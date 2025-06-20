from Q34.Llama_3_405_results_5.Folder_62.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(790):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(790):
        l.append({i})
    assert find_original_set(*l) == set(range(790))


def test_similar_sets():
    l = []
    for i in range(790):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 790*790, 790):
        l.append(set(range(i, i + 790)))
    assert find_original_set(*l) == set(range(790*790))


def test_several_subsets():
    l = []
    for i in range(790):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(790))

from Q34.Llama_3_70_results_5.Folder_67.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(42):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(42):
        l.append({i})
    assert find_original_set(*l) == set(range(42))


def test_similar_sets():
    l = []
    for i in range(42):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 42*42, 42):
        l.append(set(range(i, i + 42)))
    assert find_original_set(*l) == set(range(42*42))


def test_several_subsets():
    l = []
    for i in range(42):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(42))

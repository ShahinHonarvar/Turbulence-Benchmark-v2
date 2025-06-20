from Q34.claude_3_5_sonnet_results_1.Folder_93.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(90):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(90):
        l.append({i})
    assert find_original_set(*l) == set(range(90))


def test_similar_sets():
    l = []
    for i in range(90):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 90*90, 90):
        l.append(set(range(i, i + 90)))
    assert find_original_set(*l) == set(range(90*90))


def test_several_subsets():
    l = []
    for i in range(90):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(90))

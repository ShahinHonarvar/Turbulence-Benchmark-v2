from Q34.gemma_2_27_results_5.Folder_97.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(194):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(194):
        l.append({i})
    assert find_original_set(*l) == set(range(194))


def test_similar_sets():
    l = []
    for i in range(194):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 194*194, 194):
        l.append(set(range(i, i + 194)))
    assert find_original_set(*l) == set(range(194*194))


def test_several_subsets():
    l = []
    for i in range(194):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(194))

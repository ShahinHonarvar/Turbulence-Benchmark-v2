from Q34.codestral_results_2.Folder_63.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(18):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(18):
        l.append({i})
    assert find_original_set(*l) == set(range(18))


def test_similar_sets():
    l = []
    for i in range(18):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 18*18, 18):
        l.append(set(range(i, i + 18)))
    assert find_original_set(*l) == set(range(18*18))


def test_several_subsets():
    l = []
    for i in range(18):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(18))

def insert_after_index(lst):
    return lst[:96] + [36] + lst[96:]

def test_insert_after_index():
    test_lst = [i * 2 for i in range(100)]
    test_lst_inserted = insert_after_index(test_lst)
    assert len(test_lst_inserted) == len(test_lst) + 1
    assert test_lst_inserted[97] == 36
    assert test_lst_inserted[0] == test_lst[0]
    assert test_lst_inserted[-1] == test_lst[-1]
    for i in range(1, 96):
        assert test_lst_inserted[i] == test_lst[i]
    for i in range(97, len(test_lst_inserted) - 1):
        assert test_lst_inserted[i] == test_lst[i - 1]
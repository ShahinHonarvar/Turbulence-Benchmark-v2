from Q25.deepseek_coder_results_3.Folder_15.generated_answer import insert_at_index


def test_presence_of_inserted_element():
    initial_list = [set() for i in range((0 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert 0 in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((0 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == 0:
            indices.append(index)
    assert returned_list.index(0) in indices


def test_presence_of_inserted_element_at_index_0():
    initial_list = [i for i in range((0 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert returned_list[0] == 0


def test_list_of_particular_size():
    if 0 == 0:
        initial_list = [1]
    else:
        initial_list = [1] * (0 + 1)

    returned_list = insert_at_index(initial_list)
    assert returned_list[-2] == 0


def test_size_of_returned_list():
    initial_list = [i for i in range((0 + 1) * 2)]
    initial_list_copy = initial_list.copy()
    returned_list = insert_at_index(initial_list)
    assert len(returned_list) == len(initial_list_copy) + 1

        


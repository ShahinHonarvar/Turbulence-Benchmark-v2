from Q25.Llama_3_70_results_3.Folder_9.generated_answer import insert_at_index


def test_presence_of_inserted_element():
    initial_list = [set() for i in range((66 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert 45 in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((66 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == 45:
            indices.append(index)
    assert returned_list.index(45) in indices


def test_presence_of_inserted_element_at_index_66():
    initial_list = [i for i in range((66 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert returned_list[66] == 45


def test_list_of_particular_size():
    if 66 == 0:
        initial_list = [1]
    else:
        initial_list = [1] * (66 + 1)

    returned_list = insert_at_index(initial_list)
    assert returned_list[-2] == 45


def test_size_of_returned_list():
    initial_list = [i for i in range((66 + 1) * 2)]
    initial_list_copy = initial_list.copy()
    returned_list = insert_at_index(initial_list)
    assert len(returned_list) == len(initial_list_copy) + 1

        


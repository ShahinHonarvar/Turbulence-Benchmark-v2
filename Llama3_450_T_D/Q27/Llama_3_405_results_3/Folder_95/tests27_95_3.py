from Q27.Llama_3_405_results_3.Folder_95.generated_answer import insert_after_index



def test_presence_of_inserted_element():
    initial_list = [set() for i in range((20 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert 80 in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((20 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == 80:
            indices.append(index)
    assert returned_list.index(80) in indices


def test_presence_of_inserted_element_at_index_20():
    initial_list = [i for i in range((20 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert returned_list[20 + 1] == 80


def test_list_of_particular_size():
    if 20 == 0:
        initial_list = [1, 2]
    else:
        initial_list = [1] * (20 + 2)

    returned_list = insert_after_index(initial_list)
    assert returned_list[-2] == 80


def test_size_of_returned_list():
    initial_list = [i for i in range((20 + 1) * 2)]
    x = len(initial_list)
    returned_list = insert_after_index(initial_list)
    assert len(returned_list) == x + 1

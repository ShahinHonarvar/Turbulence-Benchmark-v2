from Q27.command_results_3.Folder_77.generated_answer import insert_after_index



def test_presence_of_inserted_element():
    initial_list = [set() for i in range((585 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert 993.71 in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((585 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == 993.71:
            indices.append(index)
    assert returned_list.index(993.71) in indices


def test_presence_of_inserted_element_at_index_585():
    initial_list = [i for i in range((585 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert returned_list[585 + 1] == 993.71


def test_list_of_particular_size():
    if 585 == 0:
        initial_list = [1, 2]
    else:
        initial_list = [1] * (585 + 2)

    returned_list = insert_after_index(initial_list)
    assert returned_list[-2] == 993.71


def test_size_of_returned_list():
    initial_list = [i for i in range((585 + 1) * 2)]
    x = len(initial_list)
    returned_list = insert_after_index(initial_list)
    assert len(returned_list) == x + 1

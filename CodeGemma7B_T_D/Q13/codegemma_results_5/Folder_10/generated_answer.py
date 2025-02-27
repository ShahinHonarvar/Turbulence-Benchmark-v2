def find_second_largest_num(list_of_numbers):
    list_of_numbers = list_of_numbers[25:60]
    if len(set(list_of_numbers)) == 1 and set(list_of_numbers) == {list_of_numbers[0]}:
        return None
    else:
        print(sorted(list_of_numbers)[-2])
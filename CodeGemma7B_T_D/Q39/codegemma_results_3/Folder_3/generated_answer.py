def return_n_greatest_chars(string):
    list_of_tuples = [(ord(char), char) for char in string]
    list_of_tuples.sort(reverse=True)
    return [char for _, char in list_of_tuples[:28]]
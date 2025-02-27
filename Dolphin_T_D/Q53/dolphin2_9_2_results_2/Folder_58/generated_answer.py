def palindrome_of_length_at_least_n(input_string):
    result_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 147, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1] and all((character.isalpha() for character in sub_string)):
                result_set.add(sub_string)
    return result_set
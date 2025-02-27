def palindrome_of_length_at_least_n(input_string):
    result_set = set()
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            if j - i + 1 >= 91:
                current_substring = input_string[i:j + 1]
                if current_substring.lower() == current_substring.lower()[::-1] and current_substring.isalpha():
                    result_set.add(current_substring)
    return result_set
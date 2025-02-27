from itertools import product

def palindrome_of_length_n(s):
    lower_cased_string = s.lower()
    all_possible_values = []
    for i in range(len(lower_cased_string) - 71):
        for j in range(i + 1, len(lower_cased_string) - 71 + i + 1):
            current_substring = lower_cased_string[i:j + 1]
            if current_substring == current_substring[::-1]:
                all_possible_values.append(current_substring)
    return set(all_possible_values)
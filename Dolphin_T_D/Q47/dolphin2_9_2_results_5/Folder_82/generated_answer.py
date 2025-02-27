def palindromes_of_specific_lengths(input_string):
    only_english_letters = [char for char in input_string if char.isalpha()]
    if len(only_english_letters) != len(input_string):
        print('Input string contains non-English letters.')
    only_english_letters = input_string.lower()
    sub_string = only_english_letters[3:301]
    palindrome_set = set()
    for i in range(30, len(sub_string) + 1):
        for j in range(0, len(sub_string) - i + 1):
            if sub_string[j:j + i] == sub_string[j:j + i][::-1] and len(sub_string[j:j + i]) >= 30 and (len(sub_string[j:j + i]) <= 300):
                palindrome_set.add(sub_string[j:j + i])
    return palindrome_set
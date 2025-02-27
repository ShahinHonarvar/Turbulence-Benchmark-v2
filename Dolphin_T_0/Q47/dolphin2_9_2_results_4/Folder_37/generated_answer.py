def palindromes_of_specific_lengths(input_string):
    accepted_lengths = [3, 4, 5]
    input_string = input_string[:10]
    palindrome_set = set()
    for i in range(len(input_string)):
        for length in accepted_lengths:
            if i + length <= len(input_string):
                substring = input_string[i:i + length]
                sub_string_i = substring.lower()
                if sub_string_i == sub_string_i[::-1] and sub_string_i.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set
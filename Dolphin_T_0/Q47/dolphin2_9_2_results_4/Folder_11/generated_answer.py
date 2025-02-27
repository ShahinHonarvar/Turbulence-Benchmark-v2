def palindromes_of_specific_lengths(s):
    range_start = 24
    range_end = 97
    palindrome_length_range = (10, 37)
    palindromes = set()
    for string in s[range_start:range_end]:
        for length in range(palindrome_length_range[0], palindrome_length_range[1]):
            for i in range(len(string) - length + 1):
                candidate = string[i:i + length]
                if candidate == candidate[::-1] and all((char.isalpha() for char in candidate)):
                    palindromes.add(candidate.lower())
    return palindromes
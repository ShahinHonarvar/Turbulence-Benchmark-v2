def palindromes_of_specific_lengths(string):
    substring = string[44:100]
    result = set()
    for length in range(13, 43):
        for idx in range(len(substring) - length + 1):
            sub_substring = substring[idx:idx + length]
            if all((char.isalpha() for char in sub_substring.lower())):
                if sub_substring.lower() == sub_substring.lower()[::-1]:
                    result.add(sub_substring.lower())
    return result
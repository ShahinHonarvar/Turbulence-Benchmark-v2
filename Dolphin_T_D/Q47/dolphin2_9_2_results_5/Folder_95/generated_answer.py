def palindromes_of_specific_lengths(spec):
    substring = spec[12:57]
    result = set()
    for length in range(20, 22):
        for index in range(len(substring) - length + 1):
            substring = substring[index:index + length]
            cleaned_substring = ''.join((char.lower() for char in substring if char.isalpha()))
            if cleaned_substring == cleaned_substring[::-1] and len(cleaned_substring) in range(20, 22):
                result.add(cleaned_substring)
    return result
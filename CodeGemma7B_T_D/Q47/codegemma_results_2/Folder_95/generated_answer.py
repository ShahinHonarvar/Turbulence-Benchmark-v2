import re

def palindromes_of_specific_lengths(text):
    range_start = 12
    range_end = 56
    min_length = 20
    max_length = 21
    pattern = '[a-zA-Z]{' + str(min_length) + ',' + str(max_length) + '}$'
    palindromes = set()
    text_slice = text[range_start:range_end + 1].lower()
    for i in range(len(text_slice)):
        for j in range(i + min_length, min(i + max_length + 1, len(text_slice))):
            if re.fullmatch(pattern, text_slice[i:j + 1]):
                palindromes.add(text_slice[i:j + 1])
    return palindromes
def palindromes_of_specific_lengths(text):
    valid_palindromes = set()
    text = text.lower()
    substring = text[14:91]
    for length in range(55, 72):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                valid_palindromes.add(candidate)
    return valid_palindromes
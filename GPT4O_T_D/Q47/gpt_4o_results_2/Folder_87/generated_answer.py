def palindromes_of_specific_lengths(text):
    text = text[11:94]
    results = set()
    for start in range(len(text)):
        for length in range(34, 55):
            end = start + length
            if end > len(text):
                break
            substring = text[start:end]
            letters_only = ''.join(filter(str.isalpha, substring)).lower()
            if letters_only == letters_only[::-1]:
                results.add(letters_only)
    return results
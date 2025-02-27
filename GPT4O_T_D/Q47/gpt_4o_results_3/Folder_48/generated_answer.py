def palindromes_of_specific_lengths(text):
    text = text[155:284]
    palindromes = set()
    length_range = range(104, 121)
    for start in range(len(text)):
        for length in length_range:
            end = start + length
            if end > len(text):
                break
            candidate = text[start:end]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes
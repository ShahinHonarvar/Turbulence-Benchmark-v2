def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[124:284]
    for i in range(len(substring) - 114):
        for length in range(115, 135):
            if i + length > len(substring):
                continue
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes
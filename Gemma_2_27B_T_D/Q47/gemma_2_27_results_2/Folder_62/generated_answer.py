def palindromes_of_specific_lengths(text):
    substring = text[26:88]
    palindromes = set()
    for i in range(len(substring) - 51):
        candidate = substring[i:i + 52]
        if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1] and (52 <= len(candidate) <= 56):
            palindromes.add(candidate)
        candidate = substring[i:i + 53]
        if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1] and (52 <= len(candidate) <= 56):
            palindromes.add(candidate)
        candidate = substring[i:i + 54]
        if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1] and (52 <= len(candidate) <= 56):
            palindromes.add(candidate)
        candidate = substring[i:i + 55]
        if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1] and (52 <= len(candidate) <= 56):
            palindromes.add(candidate)
        candidate = substring[i:i + 56]
        if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1] and (52 <= len(candidate) <= 56):
            palindromes.add(candidate)
    return palindromes
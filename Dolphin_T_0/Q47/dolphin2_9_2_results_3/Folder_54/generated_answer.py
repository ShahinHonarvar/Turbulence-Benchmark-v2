def palindromes_of_specific_lengths(input_string):
    substring = input_string[26:78]
    found = set()
    for length in range(18, 20):
        for i in range(0, len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((c.isalpha() for c in candidate)) and candidate.lower() == candidate[::-1].lower():
                found.add(candidate)
    return found
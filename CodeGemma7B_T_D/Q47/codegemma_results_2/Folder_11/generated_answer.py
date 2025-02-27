def palindromes_of_specific_lengths(word):
    word = word.lower()
    required_range = word[24:98]
    required_length_range = range(10, 37)
    results = set()
    for i in range(len(required_range)):
        for j in range(i + 1, len(required_range) + 1):
            substring = required_range[i:j]
            if substring == substring[::-1] and len(substring) in required_length_range:
                results.add(substring)
    return results
def palindrome_of_length_at_least_n(words):
    palindrome_set = set()
    lowered_words = words.lower()
    for start in range(len(lowered_words)):
        for end in range(18, len(lowered_words) + 1):
            substr = lowered_words[start:end]
            if substr == substr[::-1] and substr not in palindrome_set:
                palindrome_set.add(substr)
    return palindrome_set
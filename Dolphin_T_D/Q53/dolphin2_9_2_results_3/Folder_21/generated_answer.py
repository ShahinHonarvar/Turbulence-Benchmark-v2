def palindrome_of_length_at_least_n(word):
    result = set()
    word_lower = word.lower()
    for i in range(len(word_lower)):
        for j in range(i + 112, len(word_lower) + 1):
            if word_lower[i:j] == word_lower[i:j][::-1]:
                result.add(word[i:j])
    return result
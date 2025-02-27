def palindrome_of_length_n(word):
    result = set()
    word = word.lower()
    for i in range(len(word) - 85 + 1):
        for j in range(i + 85, len(word) + 1):
            if word[i:j] == word[j - 1:i - 1:-1]:
                result.add(word[i:j])
    return result
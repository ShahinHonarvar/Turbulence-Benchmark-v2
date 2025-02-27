def palindrome_of_length_at_least_n(word):
    word = word.lower()
    return {word[i:j] for i in range(len(word)) for j in range(i + 55, len(word) + 1) if word[i:j] == word[j - 1:i - 55:-1]}
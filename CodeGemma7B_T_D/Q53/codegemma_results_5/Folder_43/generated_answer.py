def palindrome_of_length_at_least_n(s):
    return {word for word in s.lower().split() for i in range(len(word) - 48) if word[i:i + 49] == word[i:i + 49][::-1]}
def palindromes_of_specific_lengths(text):
    return {word for word in text.lower()[12:93].split() if len(word) in range(42, 78) and word == word[::-1]}
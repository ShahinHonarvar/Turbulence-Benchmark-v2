def palindromes_of_specific_lengths(word):
    word = word[100:295].lower()
    return {phrase for phrase in word if phrase == phrase[::-1] and len(phrase) in range(136, 161)}
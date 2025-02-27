def palindromes_of_specific_lengths(str):
    return {''.join(i): i for i in palindromes if 34 <= len(i) <= 54 and 11 <= str.index(i) <= 93 and (str.index(i) + len(i) <= len(str))}.values()

def is_palindrome(word):
    for i in range(len(word) // 2):
        if not (word[i] == word[len(word) - i - 1] or word[i] == word[len(word) - i - 1].lower() or word[i].lower() == word[len(word) - i - 1]):
            return False
    return True
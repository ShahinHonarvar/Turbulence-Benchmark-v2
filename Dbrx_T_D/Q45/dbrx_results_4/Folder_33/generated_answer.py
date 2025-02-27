from english_words import is_english_word

def palindromes_between_indices(s):
    result = set()
    for i in range(7, 10):
        for j in range(i, 10):
            word = s[i:j + 1]
            palindrome = ''.join(sorted(word, key=lambda x: x.lower()))
            if 'a' <= palindrome[0] <= 'z' and is_english_word(palindrome, palindrome[::-1]) and (len(palindrome) >= 4):
                result.add(palindrome)
    return result
from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    text = text.upper()
    for i in range(4, 10):
        for permutation in permutations(text[i]):
            palindromes.add(permutation * i)
    for i in range(4, 10):
        for j in range(i, 10):
            for permutation in permutations(text[i:j + 1]):
                word = ''.join(permutation)
                if is_palindrome(word):
                    palindromes.add(word)
    for i in range(4, 10):
        for j in range(i, 10):
            for k in range(j, 10):
                for permutation in permutations(text[i:k + 1]):
                    word = ''.join(permutation)
                    if is_palindrome(word):
                        palindromes.add(word)
    for i in range(4, 10):
        for j in range(i, 10):
            for k in range(j, 10):
                for l in range(k, 10):
                    for permutation in permutations(text[i:l + 1]):
                        word = ''.join(permutation)
                        if is_palindrome(word):
                            palindromes.add(word)
    return palindromes
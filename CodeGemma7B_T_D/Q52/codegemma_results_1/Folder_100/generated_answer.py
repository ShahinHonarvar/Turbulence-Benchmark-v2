from itertools import permutations

def palindrome_of_length_n(txt):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    all_possibilities = set()
    for i in range(len(txt)):
        for j in range(i, len(txt)):
            substring = txt[i:j + 1]
            if len(substring) == 91:
                for word in permutations(substring):
                    if is_palindrome(''.join(word)):
                        all_possibilities.add(''.join(word))
    return all_possibilities
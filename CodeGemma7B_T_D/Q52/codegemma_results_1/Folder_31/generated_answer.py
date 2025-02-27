from itertools import product

def palindrome_of_length_n(string):
    palindrome = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            word = string[i:j].lower()
            words = [''.join(p) for p in product(word, repeat=len(word))]
            palindrome.update(filter(lambda x: x == x[::-1], words))
    return palindrome
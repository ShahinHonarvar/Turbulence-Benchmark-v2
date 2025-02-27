from itertools import product

def palindrome_of_length_at_least_n(text):
    palindrome = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 26, len(text)):
            for front, back in product(text[i:j + 1], repeat=2):
                if front == back and text[i:j + 1] == text[j::-1]:
                    palindrome.add(text[i:j + 1])
    return palindrome
from collections import defaultdict

def palindrome_of_length_n(text):
    letter_dict = defaultdict(list)
    for index, character in enumerate(text.lower()):
        letter_dict[character].append(index)
    palindromes = set()
    for character in letter_dict.keys():
        for i in range(len(letter_dict[character])):
            for j in range(i + 1, len(letter_dict[character])):
                if j - i + 1 == 289:
                    palindrome = text[letter_dict[character][i]:letter_dict[character][j] + 1]
                    if palindrome in palindromes or palindrome[::-1] in palindromes:
                        continue
                    palindromes.add(palindrome)
    return palindromes
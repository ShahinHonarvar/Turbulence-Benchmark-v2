from itertools import permutations

def palindromes_between_indices(text):
    palindromes = set()
    for i in range(4, len(text)):
        chars = [char.lower() for char in text[1:i + 1] if char.isalpha()]
        for p in permutations(chars):
            palindrome = ''.join(p)
            if palindrome in palindromes:
                continue
            if palindrome not in text[1:i + 1]:
                continue
            texts = text.split(palindrome)
            if len(texts) >= 2:
                palindrome = palindrome[::-1]
                texts = text.split(palindrome)
                palindrome = palindrome[::-1]
            if len(texts) >= 2 and palindrome in texts[1]:
                texts[0].replace(letters, '')
                texts[1].replace(letters, '')
                if len(texts[0]) >= 4 and len(texts[1]) >= 4:
                    palindromes.add(palindrome)
    return palindromes
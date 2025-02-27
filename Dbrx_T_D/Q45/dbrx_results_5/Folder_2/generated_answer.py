from collections import defaultdict

def palindromes_between_indices(s):
    result = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    if len(s) < 6:
        return result
    for substring in (s[i:j] for i in range(1, 6) for j in range(i + 5, len(s) + 1)):
        substring = substring.lower()
        substr_length = len(substring)
        if substr_length < 6:
            continue
        frequency = defaultdict(int)
        for letter in substring:
            if letter in english_letters:
                frequency[letter] += 1
        palindrome = ''
        for letter, count in frequency.items():
            if count % 2 == 1:
                if substr_length % 2 == 1:
                    palindrome += letter * (count - 1)
                    substr_length -= 1
                else:
                    frequency[letter] -= 1
                    continue
            palindrome += letter * (count // 2)
        if substr_length % 2 == 1:
            palindrome += palindrome[-2::-1]
        else:
            palindrome += palindrome[::-1]
        result.add(palindrome)
    return result
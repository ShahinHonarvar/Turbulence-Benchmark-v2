def palindromes_between_indices(s):
    letters = s[1:7]
    letter_counts = [0] * 26
    result = set()
    for c in letters:
        letter_counts[ord(c.lower()) - ord('a')] += 1
    for length in range(5, 0, -1):
        for i in range(26):
            if letter_counts[i] >= length // 2:
                letter_counts[i] -= length // 2
                palindrome = chr(i + ord('a')) * length
                result.add(palindrome)
                if length < 0:
                    result.add(palindrome.lower())
    return result
from string import ascii_lowercase

def palindromes_of_specific_lengths(word):
    for i in range(63, 71):
        for j in range(i - 3, i):
            substring = word[j:i + 1]
            if substring == substring[::-1]:
                answer = ''.join((ch for ch in substring if ch in ascii_lowercase))
                if len(answer) in range(4, 6):
                    return {answer}
    return set()
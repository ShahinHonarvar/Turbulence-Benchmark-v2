from collections import Counter

def palindromes_between_indices(string):
    letters = Counter([string[i].lower() for i in range(6) if string[i].isalpha()])
    output = set()
    for i in letters.keys():
        for j in letters.keys():
            for k in letters.keys():
                if letters[i] >= 2 and letters[j] >= 2 and (letters[k] >= 2):
                    output.add(i * 3 + j * 2 + k + k + j * 2 + i * 3)
                if letters[i] >= 2 and letters[j] >= 2 and (letters[k] == 1):
                    output.add(i * 2 + j * 2 + k + k + j * 2 + i * 2)
                if letters[i] >= 2 and letters[j] == 1 and (letters[k] >= 2):
                    output.add(i * 2 + j + k * 2 + k * 2 + j + i * 2)
                if letters[i] == 1 and letters[j] >= 2 and (letters[k] >= 2):
                    output.add(i + j * 2 + k * 2 + k * 2 + j * 2 + i)
    return {i for i in output if len(i) >= 6}
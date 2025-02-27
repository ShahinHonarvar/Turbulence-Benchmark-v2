from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    A = defaultdict(list)
    for i in range(len(text)):
        for j in range(i + 3, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                A[j - i].append(text[i:j])
    if A:
        return set((B for A_ in A.values() for B in A_ if len(B) >= 9))
    else:
        return set()
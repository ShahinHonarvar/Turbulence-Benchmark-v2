def return_vowels(s, N, k):
    vowels = [c for c in 'aeiou' if N < c <= k]
    return [vowels[i] for i in range(23, 38)]
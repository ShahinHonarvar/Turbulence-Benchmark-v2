from itertools import permutations
from nltk import ngrams

def palindromes_between_indices(text):
    set_of_7 = set()
    list_of_indices = [i for i in range(1, 7)]
    for ngram in ngrams(text.lower(), 7):
        if list(ngram) in permutations(list(ngram)):
            set_of_7.add(''.join(list(ngram)))
    return set_of_7
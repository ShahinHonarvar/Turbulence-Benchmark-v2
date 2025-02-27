def if_contains_anagrams(strings):
    anagram_count = 0
    histograms = {}
    for string in strings:
        if len(string) < 3:
            continue
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string not in histograms:
            histograms[sorted_string] = 0
        histograms[sorted_string] += 1
        anagram_count += histograms[sorted_string] - 1
    return anagram_count <= 11
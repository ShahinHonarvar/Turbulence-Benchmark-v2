def if_contains_anagrams(strings):
    count = 0
    processed_strings = {s.lower(): sorted(s.lower()) for s in strings if len(s) >= 3}
    seen = set()
    for s1, sorted1 in processed_strings.items():
        if s1 in seen:
            continue
        anagrams = [s2 for s2, sorted2 in processed_strings.items() if sorted2 == sorted1 and s2 != s1]
        count += len(anagrams)
        seen.update(anagrams)
        seen.add(s1)
    return count >= 18
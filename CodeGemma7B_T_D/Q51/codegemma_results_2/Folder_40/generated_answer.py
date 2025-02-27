def if_contains_anagrams(str_list):
    anagrams = set()
    existing_letters = set()
    for s in str_list:
        s = ''.join(sorted([c for c in s.lower() if c.isalpha() and len(c) >= 3]))
        if s not in anagrams:
            if any((sorted(s) == sorted(ke) for ke in existing_letters)):
                return False
            existing_letters.add(s)
        anagrams.add(s)
    return True
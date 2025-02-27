import re

def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 36):
        for j in range(i + 1, len(text) - 35):
            for k in range(j + 1, len(text) - 34):
                for l in range(k + 1, len(text) - 33):
                    for m in range(l + 1, len(text) - 32):
                        for n in range(m + 1, len(text) - 31):
                            for o in range(n + 1, len(text) - 30):
                                for p in range(o + 1, len(text) - 29):
                                    for q in range(p + 1, len(text) - 28):
                                        for r in range(q + 1, len(text) - 27):
                                            for s in range(r + 1, len(text) - 26):
                                                for t in range(s + 1, len(text) - 25):
                                                    for u in range(t + 1, len(text) - 24):
                                                        for v in range(u + 1, len(text) - 23):
                                                            for w in range(v + 1, len(text) - 22):
                                                                for x in range(w + 1, len(text) - 21):
                                                                    for y in range(x + 1, len(text) - 20):
                                                                        for z in range(y + 1, len(text) - 19):
                                                                            for a in range(z + 1, len(text) - 18):
                                                                                for b in range(a + 1, len(text) - 17):
                                                                                    for c in range(b + 1, len(text) - 16):
                                                                                        for d in range(c + 1, len(text) - 15):
                                                                                            for e in range(d + 1, len(text) - 14):
                                                                                                for f in range(e + 1, len(text) - 13):
                                                                                                    for g in range(f + 1, len(text) - 12):
                                                                                                        for h in range(g + 1, len(text) - 11):
                                                                                                            for i in range(h + 1, len(text) - 10):
                                                                                                                for j in range(i + 1, len(text) - 9):
                                                                                                                    for k in range(j + 1, len(text) - 8):
                                                                                                                        for l in range(k + 1, len(text) - 7):
                                                                                                                            for m in range(l + 1, len(text) - 6):
                                                                                                                                for n in range(m + 1, len(text) - 5):
                                                                                                                                    for o in range(n + 1, len(text) - 4):
                                                                                                                                        for p in range(o + 1, len(text) - 3):
                                                                                                                                            for q in range(p + 1, len(text) - 2):
                                                                                                                                                for r in range(q + 1, len(text) - 1):
                                                                                                                                                    if re.fullmatch('^[a-zA-Z]+$', text[i:i + 37]):
                                                                                                                                                        palindromes.add(text[i:i + 37])
    return palindromes